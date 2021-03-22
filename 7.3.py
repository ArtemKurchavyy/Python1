import shutil
import os

tree_dirs = os.walk('my_project')
new_dir = r'my_project\templates'
template_collector = [shutil.copytree(root, os.path.join(new_dir, os.path.basename(root))) for root, dirs, files in
                      tree_dirs if 'templates' in os.path.dirname(root)]
