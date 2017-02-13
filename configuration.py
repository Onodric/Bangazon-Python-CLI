import os.path

# filepath = 'c:/Users/marce/bangazon-cli/db/bangazon.db'
package_dir = os.path.abspath(os.path.dirname(__file__))
database_path = os.path.join(package_dir, 'db\\bangazon.db')
# configuration.database_path