class HttpUnprocesableEntityError(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message = message
        self.name = 'UnprocessableEntify'
        self.status_code = 422

try:
    print('Estou no block try')
    raise HttpUnprocesableEntityError('Estou lançando a exception')
except Exception as exception:
    print('Estou no tratamento de erros')
    print(exception.name)
    print(exception.status_code)
    print(exception.message)

