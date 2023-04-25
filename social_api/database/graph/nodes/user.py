from neomodel import StructuredNode, StringProperty, RelationshipTo, RelationshipFrom


class User(StructuredNode):
    username = StringProperty(unique_index=True)
    follows = RelationshipTo("User", "FOLLOWS")
    followers = RelationshipFrom("User", "FOLLOWS")
