openapi: 3.0.0
info:
  version: 1.0.0
  title: API catalog
  description: An API for registering and managing APIs in a catalog
  contact:
    name: Developer portal team
    email: developerportal@oslo.kommune.no
    url: 'https://github.oslo.kommune.no/origodigi/api-catalog-backend'
  license:
    name: Apache 2.0
    url: 'https://www.apache.org/licenses/LICENSE-2.0.html'
servers:
  - url: 'https://api-catalog.k8s.oslo.kommune.no'
paths:
  /apis:
    get:
      summary: List all the APIs in the catalog
      operationId: listApis
      responses:
        '200':
          description: OK
          content:
            'application/json':
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/SomeApi'
        '406':
          description: Missing Accept header
  '/apis/without-spec':
    post:
      summary: Adds a new API
      description: >-
        Note that the posted ID will be ignored. It's just to make the API spec
        less complex.
      operationId: addApiWithoutSpec
      security:
        - oAuth: []
      responses:
        '200':
          description: Success
          content:
            application/json:
              schema:
                type: object
                properties:
                  id:
                    type: integer
                    format: int64
                    description: >-
                      The API that was stored, with a generated ID for future
                      reference.
        '400':
          description: Bad request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/BadRequestError'
        '401':
          description: Unauthorized
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/UnauthorizedError'
        '404':
          description: Resource Not Found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/NotFoundError'
        '405':
          description: Resource creation conflict
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ConflictError'
        '406':
          description: Missing Accept header
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/NotAcceptableError'
      requestBody:
        $ref: '#/components/requestBodies/SomeApiWithoutSpec'
  '/apis/with-spec':
    post:
      summary: Adds a new API
      description: >-
        Note that the posted ID will be ignored. It's just to make the API spec
        less complex.
      operationId: addApiWithSpec
      security:
        - oAuth: []
      responses:
        '200':
          description: Success
          content:
            application/json:
              schema:
                type: object
                properties:
                  id:
                    type: integer
                    format: int64
                    description: >-
                      The API that was stored, with a generated ID for future
                      reference.
        '400':
          description: Bad request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/BadRequestError'
        '401':
          description: Unauthorized
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/UnauthorizedError'
        '404':
          description: Resource Not Found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/NotFoundError'
        '405':
          description: Resource creation conflict
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ConflictError'
        '406':
          description: Missing Accept header
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/NotAcceptableError'
      requestBody:
        $ref: '#/components/requestBodies/SomeApiWithSpec'
  '/apis/{id}':
    get:
      summary: Gets API by ID
      operationId: getApi
      parameters:
        - $ref: '#/components/parameters/id'
      responses:
        '200':
          description: OK
          content:
            '*/*':
              schema:
                $ref: '#/components/schemas/SomeApi'
        '400':
          description: Invalid ID supplied
        '404':
          description: API not found
        '406':
          description: Missing Accept header
          content:
            '*/*':
              schema:
                $ref: '#/components/schemas/NotAcceptableError'
    put:
      summary: Updates an existing API
      operationId: updateApi
      description: >-
        Note that the ID in SomeApi will be ignored. It's just to make the API spec
        less complex.

        When supplying a Swagger or OpenApi specificaion url, the specification will be parsed
        and updated with information from the spec. Other fields will then be ignored.

        If not supplying a specification url, the api will be updated with information
        from the other fields.
      security:
        - oAuth: []
      parameters:
        - $ref: '#/components/parameters/id'
      responses:
        '200':
          description: Success
        '406':
          description: Missing Accept header
          content:
            '*/*':
              schema:
                $ref: '#/components/schemas/NotAcceptableError'
      requestBody:
        $ref: '#/components/requestBodies/SomeApi'
    delete:
      summary: Deletes the given API
      operationId: deleteApi
      security:
        - oAuth: []
      parameters:
        - $ref: '#/components/parameters/id'
      responses:
        '204':
          description: API deleted
        '400':
          description: Invalid ID supplied
        '404':
          description: API not found
        '406':
          description: Missing Accept header
          content:
            '*/*':
              schema:
                $ref: '#/components/schemas/NotAcceptableError'
  '/apis/{id}/spec':
    get:
      summary: Get Api's Swagger/OpenApi specification
      operationId: getApiSpecification
      parameters:
        - $ref: '#/components/parameters/id'
      responses:
        '200':
          description: OK
          content:
            text/plain:
              schema:
                type: string
        '400':
          description: Invalid ID supplied
        '404':
          description: API not found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/NotFoundError'
        '406':
          description: Missing Accept header
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/NotAcceptableError'
  '/apis/access':
      get:
        summary: Get all API keys for authenticated user
        operationId: getApiKeysForUser
        security:
          - oAuth: []
        responses:
          '200':
            description: OK
            content:
              '*/*':
                schema:
                  type: array
                  items:
                    $ref: '#/components/schemas/ApiKey'
          '401':
            description: Unauthorized
            content:
              application/json:
                schema:
                  $ref: '#/components/schemas/UnauthorizedError'
          '406':
            description: Missing Accept header
            content:
              application/json:
                schema:
                  $ref: '#/components/schemas/NotAcceptableError'
  '/apis/{id}/access':
      get:
        summary: Get all keys for this API
        operationId: getApiKeys
        security:
        - oAuth: []
        parameters:
          - $ref: '#/components/parameters/id'
        responses:
          '200':
            description: OK
            content:
              '*/*':
                schema:
                  type: array
                  items:
                    $ref: '#/components/schemas/ApiKey'
          '401':
            description: Unauthorized
            content:
              application/json:
                schema:
                  $ref: '#/components/schemas/UnauthorizedError'
          '403':
            description: Forbidden
            content:
              application/json:
                schema:
                  type: string
                  description: You cannot list the keys for this API as you are not the owner.
                  example: You cannot get API keys for an API you do not own.
          '404':
            description: API not found
            content:
              application/json:
                schema:
                  $ref: '#/components/schemas/NotFoundError'
          '406':
            description: Missing Accept header
            content:
              application/json:
                schema:
                  $ref: '#/components/schemas/NotAcceptableError'
      post:
        summary: Request a new API key to be able to access the API
        operationId: addApiKey
        security:
        - oAuth: []
        parameters:
          - $ref: '#/components/parameters/id'
        responses:
          '200':
            description: Success
            content:
              application/json:
                schema:
                  $ref: '#/components/schemas/ApiKey'
          '400':
            description: Invalid email address
            content:
              '*/*':
                schema:
                  $ref: '#/components/schemas/BadRequestError'
          '401':
            description: Unauthorized
            content:
              application/json:
                schema:
                  $ref: '#/components/schemas/UnauthorizedError'
          '403':
            description: You have to contact the API owner to get access.
            content:
              application/json:
                schema:
                  type: string
                  description: |
                    States that you can not get access to the requested API. The response is constant and
                    will always be the one in the example.
                  example: |
                    The API owner does not allow access keys to be automatically generated. You have to manually contact
                    the API owner and ask for access.
          '404':
            description: API not found
            content:
              application/json:
                schema:
                  $ref: '#/components/schemas/NotFoundError'
        requestBody:
          $ref: '#/components/requestBodies/AccessRequest'
  '/apis/{id}/access/consumer':
      get:
        summary: Get all consumers for this API
        operationId: getApiConsumers
        parameters:
        - $ref: '#/components/parameters/id'
        responses:
          '200':
            description: OK
            content:
              '*/*':
                schema:
                  type: array
                  items:
                    $ref: '#/components/schemas/ApiConsumer'
          '401':
            description: Unauthorized
            content:
              application/json:
                schema:
                  $ref: '#/components/schemas/UnauthorizedError'
          '403':
            description: Forbidden
            content:
              application/json:
                schema:
                  type: string
                  description: You cannot list the consumers for this API as you are not the owner.
                  example: You cannot get API consumers for an API you do not own.
          '404':
            description: API not found
            content:
              application/json:
                schema:
                  $ref: '#/components/schemas/NotFoundError'
          '406':
            description: Missing Accept header
            content:
              application/json:
                schema:
                  $ref: '#/components/schemas/NotAcceptableError'
  '/specification/summary':
    get:
      summary: Get summary from a Swagger/OpenApi specification
      operationId: extractApiSpecSummary
      parameters:
        - $ref: '#/components/parameters/apiSpecificationUrl'
      responses:
        '200':
          description: Summary extracted from url
          content:
            '*/*':
              schema:
                $ref: '#/components/schemas/apiSpecSummary'
        '400':
          description: Invalid specification url
          content:
            '*/*':
              schema:
                $ref: '#/components/schemas/InvalidSpecificationError'
        '406':
          description: Missing Accept header
          content:
            '*/*':
              schema:
                $ref: '#/components/schemas/NotAcceptableError'
  '/specification/upload':
    post:
      summary: Upload an api specification file
      operationId: uploadApiSpecificationFile
      security:
        - oAuth: []
      responses:
        '201':
          description: Temporary accessable url to uploaded resource
          content:
            'application/text':
              schema:
                type: string
                description: Temporary accessable url to uploaded resource
        '400':
          description: Invalid api specification
          content:
            '*/*':
              schema:
                $ref: '#/components/schemas/InvalidSpecificationError'
        '406':
          description: Missing Accept header
          content:
            '*/*':
              schema:
                $ref: '#/components/schemas/NotAcceptableError'
      requestBody:
        content:
          multipart/form-data:
            schema:
              type: object
              required:
                - file
              properties:
                file:
                  type: string
                  # NOTE: using format: binary is currently buggy in swagger-codegen and results in a byte array which is wrong.
                  format: binary
                  description: File with api specification in swagger/openapi format
  '/apigateway/services':
    get:
      summary: Get all registered gateway services
      operationId: getGatewayServices
      security:
        - oAuth: []
      responses:
        '401':
          description: Unauthorized
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/UnauthorizedError'
        '200':
          description: Summary extracted from url
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiGatewayServices'
  '/apigateway/routes/prefixurl':
    post:
      summary: Check whether or not prefix for URL is valid and does not already exist in the gateway
      operationId: validateRouteUrlPrefix
      security:
       - oAuth: []
      responses:
        '200':
          description: Prefix is valid and does not exist in the gateway
        '400':
          description: Prefix URL is invalid.
        '401':
          description: Unauthorized
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/UnauthorizedError'
        '409':
          description: URL with prefix already exist in the gateway.
      requestBody:
        description: URL prefix to validate
        required: true
        content:
          text/plain:
            schema:
              type: string

components:
  securitySchemes:
    oAuth:
      type: oauth2
      description: This API uses OAuth 2 with the Authorization Code grant flow (Actually OIDC but swagger does not support it properly).
      flows:
        authorizationCode:
          authorizationUrl: 'https://login.oslo.kommune.no/auth/realms/api-catalog/protocol/openid-connect/auth'
          tokenUrl: 'https://login.oslo.kommune.no/auth/realms/api-catalog/protocol/openid-connect/token'
          scopes: {}
  parameters:
    id:
      name: id
      required: true
      description: The ID of the API
      in: path
      schema:
        type: integer
        format: int64
    apiSpecificationUrl:
      name: apiSpecificationUrl
      required: true
      in: query
      description: Full url for api specification
      schema:
        type: string
  requestBodies:
    SomeApi:
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/SomeApi'
      description: An API provided by some third party
      required: true
    SomeApiWithoutSpec:
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/SomeApiWithoutSpec'
      description: An API without OpenApi/Swagger specification provided by some third party
      required: true
    SomeApiWithSpec:
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/SomeApiWithSpec'
      description: An API with OpenApi/Swagger specification provided by some third party
      required: true
    AccessRequest:
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/UserInfo'
      description: The consumer of the API
      required: true
  schemas:
    apiSpecSummary:
      type: object
      required:
        - contact
        - description
        - version
        - title
      properties:
        contact:
          $ref: '#/components/schemas/ApiContact'
        description:
          type: string
          example: This is the description of my api
        version:
          type: string
          example: 2.1.0
        title:
          type: string
          description: The name of the API
          example: Weather data
        endpoint:
          type: array
          items:
              type: string
          description: The endpoint of the API
          example: www.someApi.com/apis
    ApiGatewayServices:
      type: array
      items:
        $ref: '#/components/schemas/ApiGatewayService'
    ApiGatewayService:
      type: object
      required:
        - name
      properties:
        name:
          type: string
          description: Name of service
          example: WeatherService
    SomeApi:
      type: object
      required:
        - name
        - contact
        - description
      properties:
        id:
          type: integer
          format: int64
          description: A unique ID of the API
          example: 63
        name:
          type: string
          description: The name of the API
          example: Weather data
        accessDetails:
          $ref: '#/components/schemas/AccessDetails'
        apiSpecificationUrl:
          type: string
          description: The URL the the API's specification
          example: 'http://weather.com/api/api.yaml'
        endpointUrl:
          type: string
          description: The URL of the API's endpoint
          example: 'http://weather.com/api'
        contact:
          $ref: '#/components/schemas/ApiContact'
        accessProtocol:
          $ref: '#/components/schemas/AccessProtocol'
        description:
          type: string
          description: A description of the API
          example: Provides real time weather data
        extendedDescription:
          type: string
          description: An extended description of the API, which allows for more details and markdown formatting
          example: Provides real time weather data, seriously, real time!
        whenToUse:
          type: array
          items:
            type: string
          maxItems: 3
          description: >-
            A list of example use cases for when one might want to use this API.
            Each use case will be prefixed with the text "Use this API when
            [your text]".
          example:
            - You want to check the weather for any location in the world
            - You need updated weather data no older than 10 minutes
        owner:
          type: string
          description: The name of the owner of the API
          example: Jane Doe

    SomeApiWithoutSpec:
      type: object
      required:
        - name
        - contact
      properties:
        id:
          type: integer
          format: int64
          description: A unique ID of the API
          example: 63
        name:
          type: string
          description: The name of the API
          example: Weather data
        accessDetails:
          $ref: '#/components/schemas/AccessDetails'
        endpointUrl:
          type: string
          description: The URL of the API's endpoint
          example: 'http://weather.com/api'
        contact:
          $ref: '#/components/schemas/ApiContact'
        accessProtocol:
          $ref: '#/components/schemas/AccessProtocol'
        description:
          type: string
          description: A description of the API
          example: Provides real time weather data
        extendedDescription:
          type: string
          description: An extended description of the API, which allows for more details and markdown formatting
          example: Provides real time weather data, seriously, real time!
        whenToUse:
          type: array
          items:
            type: string
          maxItems: 3
          description: >-
            A list of example use cases for when one might want to use this API.
            Each use case will be prefixed with the text "Use this API when
            [your text]".
          example:
            - You want to check the weather for any location in the world
            - You need updated weather data no older than 10 minutes
    SomeApiWithSpec:
      type: object
      required:
        - apiSpecificationUrl
      properties:
        id:
          type: integer
          format: int64
          description: A unique ID of the API
          example: 63
        accessDetails:
          $ref: '#/components/schemas/AccessDetails'
        apiSpecificationUrl:
          type: string
          description: The URL the the API's specification
          example: 'http://weather.com/api/api.yaml'
        extendedDescription:
          type: string
          description: An extended description of the API, which allows for more details and markdown formatting
          example: Provides real time weather data, seriously, real time!
    AccessDetails:
      type: object
      required:
        - accessLevel
      properties:
        accessLevel:
          $ref: '#/components/schemas/AccessLevel'
        gatewayServiceName:
          type: string
          description: The name of the service in the API gateway to connect this API to.
          example: weather-api
        gatewayRouteHostUrlPrefix:
          type: string
          description: The prefix for this API's gateway URL.
          example: my-app, could give full URL my-app.api.oslo.kommune.no
    AccessLevel:
      type: string
      description: The type of API access level configured
      example: NO_ACCESS
      enum: [NO_ACCESS, AUTOMATIC_API_KEY]
    ApiConsumer:
      type: object
      required:
        - email
        - username
        - apiKey
      properties:
        email:
          type: string
          description: The API consumer's email
          example: johndoe@mail.com
        username:
          type: string
          description: The API consumer's username
          example: johndoe
        apiKey:
          $ref: '#/components/schemas/ApiKey'
    ApiContact:
      type: object
      required:
        - name
        - email
      properties:
        name:
          type: string
          description: The API contact's name
          example: John Doe
        email:
          type: string
          description: The API contact's e-mail
          example: johndoe@mail.com
        url:
          type: string
          description: URL to a contact or support page
    ApiKey:
      type: object
      required:
        - id
        - key
        - email
      properties:
        id:
          type: string
          description: Reference ID of the created API key
          example: 265c3420-62b2-4dad-a634-445c8bcbd582
        key:
          type: string
          description: The api key
          example: lkV2AuLw39drJwMh14DB3UXHM61NSEks
        created:
          type: string
          format: date-time
          description: |
            Time and date of when the API was created. See OpenAPI specification for exact format standard.
          example: 2017-07-21T17:32:28Z
    AccessProtocol:
      type: string
      enum:
        - REST
        - SOAP
    UserInfo:
      description: Information about a user
      type: object
      required:
        - email
      properties:
        email:
          type: string
          description: The user's e-mail
          example: johndoe@mail.com

    BadRequestError:
      type: object
      allOf:
        - $ref: '#/components/schemas/Error'
      properties:
        httpStatusCode:
          type: integer
          format: int32
          example: 400
        internalCode:
          type: string
          example: APIC1006
        userMessage:
          type: string
          example: api is not valid
        internalMessage:
          type: string
          example: api is not valid
        moreInfo:
          type: string
          example: >-
            https://github.oslo.kommune.no/origodigi/api-catalog-backend/blob/master/errorCodes.md#APIC1006
    UnauthorizedError:
      type: object
      allOf:
        - $ref: '#/components/schemas/Error'
      properties:
        httpStatusCode:
          type: integer
          format: int32
          example: 401
        internalCode:
          type: string
          example: APIC1007
        userMessage:
          type: string
          example: You haven't provided a valid access token
        internalMessage:
          type: string
          example: Unauthorized
        moreInfo:
          type: string
          example: >-
            https://github.oslo.kommune.no/origodigi/api-catalog-backend/blob/master/errorCodes.md#APIC1007
    ForbiddenError:
      type: object
      allOf:
        - $ref: '#/components/schemas/Error'
      properties:
        httpStatusCode:
          type: integer
          format: int32
          example: 403
        internalCode:
          type: string
          example: APIC1008
        userMessage:
          type: string
          example: The provided access token isn't authorized to do this
        internalMessage:
          type: string
          example: Forbidden
        moreInfo:
          type: string
          example: >-
            https://github.oslo.kommune.no/origodigi/api-catalog-backend/blob/master/errorCodes.md#APIC1008
    NotFoundError:
      type: object
      allOf:
        - $ref: '#/components/schemas/Error'
      properties:
        httpStatusCode:
          type: integer
          format: int32
          example: 404
        internalCode:
          type: string
          example: APIC1003
        userMessage:
          type: string
          example: API not found
        internalMessage:
          type: string
          example: Api with id not found in db
        moreInfo:
          type: string
          example: >-
            https://github.oslo.kommune.no/origodigi/api-catalog-backend/blob/master/errorCodes.md#APIC1003
    InvalidSpecificationError:
      # allOf does not work when we also want to add our own field, in this case SchemaValidationErrors
      # So, therefore we reimplement Error Object here
      type: object
      required:
        - schemaValidationErrors
        - httpStatusCode
        - internalCode
        - userMessage
        - internalMessage
        - moreInfo
      properties:
        schemaValidationErrors:
          type: array
          items:
            $ref: '#/components/schemas/SchemaValidationError'
        httpStatusCode:
          type: integer
          format: int32
          example: 404
        internalCode:
          type: string
          example: APIC1011
        userMessage:
          type: string
          example: There was an error when trying to parse the API specification.
        internalMessage:
          type: string
          example: >-
            When retrieving the specification at the specificed URL, we were not
            able to get anything.
        moreInfo:
          type: string
          example: >-
            https://github.oslo.kommune.no/origodigi/api-catalog-backend/blob/master/errorCodes.md#APIC1011
    SchemaValidationError:
      type: object
      properties:
        keyword:
          type: string
          description: Gives an indication as to what the problem is, for example required field missing
          example: required
        message:
          type: string
          description: validation error message
          example: Field X is missing
        missing:
          type: array
          items:
            type: string
            description: missing field
            example: title
          description: list of missing fields
        specPointer:
          type: string
          description: Tries to give an indication as to where in the supplied specification the validation failed
          example: "/info"
        schemaPointer:
          type: string
          description: Tries to give an indication as to what in the official Swagger/openAPi specification the validation failed against
          example: "/definitions/info"
    NotAcceptableError:
      type: object
      allOf:
        - $ref: '#/components/schemas/Error'
      properties:
        httpStatusCode:
          type: integer
          format: int32
          example: 406
        internalCode:
          type: string
          example: APIC1004
        userMessage:
          type: string
          example: The request is missing the Accept header
        internalMessage:
          type: string
          example: The request is missing the Accept header
        moreInfo:
          type: string
          example: >-
            https://github.oslo.kommune.no/origodigi/api-catalog-backend/blob/master/errorCodes.md#APIC1004
    ConflictError:
      type: object
      allOf:
        - $ref: '#/components/schemas/Error'
      properties:
        httpStatusCode:
          type: integer
          format: int32
          example: 409
        internalCode:
          type: string
          example: APIC1002
        userMessage:
          type: string
          example: 'Conflict in resource, this resource already exists.'
        internalMessage:
          type: string
          example: Conflict
        moreInfo:
          type: string
          example: >-
            https://github.oslo.kommune.no/origodigi/api-catalog-backend/blob/master/errorCodes.md#APIC1002
    UnexpectedError:
      type: object
      allOf:
        - $ref: '#/components/schemas/Error'
      properties:
        httpStatusCode:
          type: integer
          format: int32
          example: 500
        internalCode:
          type: string
          example: APIC1009
        userMessage:
          type: string
          example: >-
            Oops, something went wrong. The error has been logged and will be
            investigated.
        internalMessage:
          type: string
          example: Unexpected error.
        moreInfo:
          type: string
          example: >-
            https://github.oslo.kommune.no/origodigi/api-catalog-backend/blob/master/errorCodes.md#APIC1009
    ServiceUnavailableError:
      type: object
      allOf:
        - $ref: '#/components/schemas/Error'
      properties:
        httpStatusCode:
          type: integer
          format: int32
          example: 503
        internalCode:
          type: string
          example: APIC1010
        userMessage:
          type: string
          example: >
            The service is currently unavailable due to a dependent service
            being down. This error has been logged and

            will be investigated.
        internalMessage:
          type: string
          example: 'The api catalog is unavailable, so we cannot process this request.'
        moreInfo:
          type: string
          example: >-
            https://github.oslo.kommune.no/origodigi/api-catalog-backend/blob/master/errorCodes.md#APIC1010
    Error:
      type: object
      discriminator:
        propertyName: internalCode
      required:
        - httpStatusCode
        - internalCode
        - userMessage
        - internalMessage
        - moreInfo
      properties:
        httpStatusCode:
          type: integer
          format: int32
          example: 500
        internalCode:
          type: string
          example: APIC1009
        userMessage:
          type: string
          example: 'Ops, something went wrong'
        internalMessage:
          type: string
          example: Internal server error
        moreInfo:
          type: string
          example: >-
            https://github.oslo.kommune.no/origodigi/api-catalog-backend/blob/master/errorCodes.md#APIC1009

