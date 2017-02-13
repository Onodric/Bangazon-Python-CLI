import os.path
package_dir = os.path.abspath(os.path.dirname(__file__))
database_path = os.path.join(package_dir, 'db/bangazon.db')



# the line below is what must be used within the modules INSTEAD of the
# relative path to the database



# configuration.database_path
