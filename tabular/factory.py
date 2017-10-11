# -*- coding: utf-8 -*-

from goerr import err


class TableController():

    def generate(self, slug, query, fields):
        html = '<table id="table_' + slug + '" class="tabular-table">'
        html += "<tr>"
        for field in fields:
            name = field
            try:
                name = query[0]._meta.get_field(field).verbose_name.title()
            except:
                pass
            html += '<th>' + name + '</th>'
        html += "</tr>"
        for row in query:
            html += "<tr>"
            for field in fields:
                try:
                    val = getattr(row, field)
                    html += '<td>' + str(val) + '</td>'
                except Exception as e:
                    err.new(e)
            html += "</tr>"
        html += '</table>'
        return html


table = TableController()
