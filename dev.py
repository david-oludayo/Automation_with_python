from user import User
from post import Post

app_user_one = User("dd@dd.com", "David", "<PASSWORD>", "DevOps Engineer")
app_user_one.get_user_info()

app_user_two = User("aa@aa.com", "John", "<PASSWORD>", "Software Engineer")
app_user_two.get_user_info()

new_post = Post("on a secret mission today", app_user_two.name)
new_post.get_post_info()
