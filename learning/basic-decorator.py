def p_decorate(func):
    def func_wrapper(name):
        return "<p>{0}</p>".format(func(name))
    return func_wrapper

@p_decorate
def get_text(name):
    return "lorem ipsum, {0} dolor sit amet".format(name)

def make_exclamatory(func):
    def wrap_func():
        return func() + "!"
    return wrap_func

@make_exclamatory
def hello_world():
    return "Hello world"

print(get_text("John"))
print(hello_world())