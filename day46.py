#!/usr/bin/env python3

# We can also use the with statement with Classes.
# They must implement the __enter__ and the __exit__ methods.
class Connection(object):
    # the __enter__ method is executed at the start of the with block
    def __enter__(self):
        # do something
        return self

    # the __exit__ method is executed at the end of the with block
    def __exit__(self, *args, **kwargs):
        # do more
        print("Disconnecting...")

    def query(self, query):
        print(query)


with Connection() as conn:
    print("Lets make a some queries!")
    conn.query("Marco")
    conn.query("Polo!")

print("Connection is no more.")
