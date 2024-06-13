from app.dependencies.user import get_current_user_dependency

def test(user: get_current_user_dependency):
    return {"message": f"{user.username} You're accessing procted route!"}