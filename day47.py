import strawberry

@strawberry.type
class Person:
    name: str
    age: int

@strawberry.type
class Book:
    title: str
    author: Person

@strawberry.type
class Query:
    @strawberry.field
    def person(self) -> Person:
        return Person(name="Tolkien", age=200)

    @strawberry.field
    def book(self) -> Book:
        return Book(title="The Hobbit", author=Person(name="Tolkien", age=200))


schema = strawberry.Schema(query=Query)

# We can then query our little graphQL application
# { book { title author { name age } } }
# or
# {person { age name } }