from user import User
from post import Post
app_user_one = User("ab@gmail.com", "Ab", "pwd1", "Devops Engineer")
app_user_one.get_user_info()
app_user_one.change_job_title("SRE")
app_user_one.get_user_info()

app_user_two = User("ww@gmail.com", "ww", "pwd2", "Developer")
app_user_two.get_user_info()

new_post = Post("I am learning", "ABC")
new_post.get_post_info()