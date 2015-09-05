from .language.ast import ListType, NonNullType, NamedType
from .type.definition import GraphQLList, GraphQLNonNull


def type_from_ast(schema, input_type_ast):
    if isinstance(input_type_ast, ListType):
        inner_type = type_from_ast(schema, input_type_ast.type)
        if inner_type:
            return GraphQLList(inner_type)
        else:
            return None
    if isinstance(input_type_ast, NonNullType):
        inner_type = type_from_ast(schema, input_type_ast.type)
        if inner_type:
            return GraphQLNonNull(inner_type)
        else:
            return None
    assert isinstance(input_type_ast, NamedType), 'Must be a type name.'
    return schema.get_type(input_type_ast.name.value)


def is_nullish(value):
    return value is None or value != value
