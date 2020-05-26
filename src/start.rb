require 'json'

def entrypoint(event:, context:)
    # TODO implement
    { statusCode: 200, body: JSON.generate('Lambda!') }
end
