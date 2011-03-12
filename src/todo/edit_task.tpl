%# 编辑一个任务的模板
%# 模板期望接收一个“no”值和一个“old”值，被选的 ToDo 项目的文本
<p>编辑 ID 为 {{no}} 的任务</p>
<form action="/edit/{{no}}" method="GET">
<input type="text" name="task" value="{{old[0]}}" size="100" maxlength="100" />
<select name="status">
<option>开启</option>
<option>关闭</option>
</select>
<br />
<input type="submit" name="save" value="save" /> <a href="http://localhost:8080/todo"></a>
</form>