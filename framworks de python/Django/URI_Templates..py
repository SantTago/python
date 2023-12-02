from uritemplate import URITemplate, expand


# NOTA: os parâmetros URI devem ser strings e não inteiros

gist_uri = 'https://api.github.com/users/sigmavirus24/gists{/gist_id}'
t = URITemplate(gist_uri)
print(t.expand(gist_id='123456'))
# => https://api.github.com/users/sigmavirus24/gists/123456

# or
print(expand(gist_uri, gist_id='123456'))

# also
t.expand({'gist_id': '123456'})
print(expand(gist_uri, {'gist_id': '123456'}))