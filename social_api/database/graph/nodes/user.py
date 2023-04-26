from neomodel import StructuredNode, StringProperty, RelationshipTo, RelationshipFrom


class User(StructuredNode):
    username = StringProperty(unique_index=True)
    follows = RelationshipTo("User", "FOLLOWS")
    followers = RelationshipFrom("User", "FOLLOWS")

    def get_all_following_users(self):
        return [follow.username for follow in self.follows.all()]

    def get_all_followers(self):
        return [follower.username for follower in self.followers.all()]
