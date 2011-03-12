%# 模板从一个元组的列表（或列表的列表、或元组的元组、或...）生成一个 HTML 表格
<p>开启的项目如下：</p>
<table border="1">
%for row in rows:
    <tr>
        <td>{{row[0]}}</td><td><a href="http://localhost:8080/edit/{{row[0]}}">{{row[1]}}</a></td>
    </tr>
%end
</table>
<a href="http://localhost:8080/new">new</a>