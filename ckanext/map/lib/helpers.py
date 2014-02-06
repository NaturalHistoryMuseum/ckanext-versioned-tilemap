# From http://stackoverflow.com/questions/5631078/sqlalchemy-print-the-actual-query

def interpolateQuery(statement, bind=None):
    """
    print a query, with values filled in
    for debugging purposes *only*
    for security, you should always separate queries from their values
    please also note that this function is quite slow
    """
    import sqlalchemy.orm
    if isinstance(statement, sqlalchemy.orm.Query):
        if bind is None:
            bind = statement.session.get_bind(
                    statement._mapper_zero_or_none()
            )
        statement = statement.statement
    elif bind is None:
        bind = statement.bind

    dialect = bind.dialect
    compiler = statement._compiler(dialect)
    class LiteralCompiler(compiler.__class__):
        def visit_bindparam(
                self, bindparam, within_columns_clause=False,
                literal_binds=False, **kwargs
        ):
            return super(LiteralCompiler, self).render_literal_bindparam(
                    bindparam, within_columns_clause=within_columns_clause,
                    literal_binds=literal_binds, **kwargs
            )

    compiler = LiteralCompiler(dialect, statement)
    return compiler.process(statement)


# From the sqlalchemy documentation itself

from sqlalchemy import func
from sqlalchemy.types import UserDefinedType

class Geometry(UserDefinedType):
    def get_col_spec(self):
        return "GEOMETRY"

    def bind_expression(self, bindvalue):
        return func.ST_GeomFromText(bindvalue, type_=self)

    def column_expression(self, col):
        return col

# MapnikPlaceholderColumn

# Mapnik accepts 'placeholders' in the sql, in the format of "!placeholder!". This is then substituted with the
# correct values at run-time. Unfortunately, of course "where(bar = !foo!)" isn't valid SQL, so we need to
# trick SQLAlchemy into outputting the placeholders by defining our own custom column format.

# See https://github.com/mapnik/mapnik/wiki/PostGIS#wiki-bbox-token for the tokens that mapnik supports

from sqlalchemy.ext.compiler import compiles
from sqlalchemy.sql.expression import ColumnClause

class MapnikPlaceholderColumn(ColumnClause):
    pass

@compiles(MapnikPlaceholderColumn)
def compile_mapnikplaceholdercolumn(element, compiler, **kw):
    return "!%s!" % element.name
