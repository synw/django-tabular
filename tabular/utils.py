# -*- coding: utf-8 -*-

import os
from django.conf import settings
from django.utils._os import safe_join
from goerr import err


def _write_file(slug, html):
    """
    Writes a table's html to a file
    """
    # check directories
    folderpath = safe_join(settings.BASE_DIR, "templates/tabular")
    if not os.path.isdir(folderpath):
        try:
            os.makedirs(folderpath)
        except Exception as e:
            err.new(e)
    endpath = "tables"
    tablesdir_path = safe_join(
        settings.BASE_DIR, "templates/tabular/" + endpath)
    if not os.path.isdir(tablesdir_path):
        try:
            os.makedirs(tablesdir_path)
        except Exception as e:
            err.new(e)
    # check file
    filepath = tablesdir_path + "/" + slug + ".html"
    #~ write the file
    try:
        filex = open(filepath, "w")
        filex.write(html)
        filex.close()
    except Exception as e:
        err.new(e)
    if err.exists:
        err.throw()