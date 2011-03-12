%# 一个新任务的表单的模板
<p>添加一个新任务到“待办事宜”：</p>
<form action="/new" method="GET">
<input type="text" size="100" maxlength="100" name="task" />
<input type="submit" name="save" value="save" />
</form>