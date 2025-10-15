---
theme: gaia
_class: lead
paginate: true
backgroundColor: #fff
backgroundImage: url('../presentations/background.svg')
---

![bg left:40% 80%](../presentations/mcp.svg)

# **HTTP Transport**

---
# HTTP Transport
## Client to Server
- Sends POST JSON-RPC requests to the server

### Server to client
- Uses Streamable HTTP
- A client may open a connection which the server can use to push messages to the client

---

# Authentication

**How difficult it can be?**

---

## Rest service authentication

1. The microservice has to obtain **client credentials**
2. The user wants to use the microservice
3. The microservice starts **PKCE flow** with the authorization server
4. The user authenticates and authorizes the microservice
5. The authorization server redirects the user back to the microservice with an authorization code
6. The microservice sends the **authorization code**, client id, and code verifier to the authorization server

---
7. The authorization server returns an **access token** (and optionally a refresh token) to the microservice
8. The microservice uses the access token to **access protected resources** on behalf of the user
9. The microservice may use the refresh token to obtain a new access token when the current one expires

**Easy, isn't it?**

---

# Why is it this "simple"?
- We have only a single client to register and can do it manually
- We know the location of the authorization server and the endpoints

vs

- How do we register every possible client?
- How do we know the location of the authorization server and the endpoints?

---

# Client Registration

- MCP server acts as a client to the resource server
- The authentication server must know the client (MCP server) before it is allowed to access resources
- The client registration is typically manual

**How can we enable every possible run of our MCP server?**

---

# Dynamic Client Registration [RFC 7591](https://datatracker.ietf.org/doc/html/rfc7591)

- The client can register itself with the authorization server
- The client sends a registration request to the authorization server's registration endpoint
- The request includes information about the client, such as its name, redirect URIs, and
  grant types
- The authorization server responds with a client ID and optionally a client secret

---

# How does the MCP client know how and where to authenticate?

- Claude Desktop doesn't know the authorization server and how to authenticat

**The MCP server must teach it**

---

# Protected Resource Metadata

[RFC 9728](https://datatracker.ietf.org/doc/html/rfc9728#name-www-authenticate-response)

# Authorization Server Metadata Discovery

[RFC 8414](https://datatracker.ietf.org/doc/html/rfc8414)

---
# Protected Resource Metadata
1. The client sends a request to the MCP server
2. The MCP server responds with a `401 Unauthorized` status code and includes a `WWW-Authenticate` header in the response
3. The client parses the `WWW-Authenticate` header to extract the URL of the authorization server's metadata endpoint

or

1. The client reads https://example.com/.well-known/oauth-protected-resource before sending the first request

---
# Server metadata

```json
 {
  "issuer":
    "https://server.example.com",
  "authorization_endpoint":
    "https://server.example.com/authorize",
  "token_endpoint":
    "https://server.example.com/token",
  "token_endpoint_auth_methods_supported":
    ["client_secret_basic", "private_key_jwt"],
  "token_endpoint_auth_signing_alg_values_supported":
    ["RS256", "ES256"],
  "userinfo_endpoint":
    "https://server.example.com/userinfo",
  "jwks_uri":
    "https://server.example.com/jwks.json",
  "registration_endpoint":
    "https://server.example.com/register",
  "scopes_supported":
    ["openid", "profile", "email", "address",
     "phone", "offline_access"],
  "response_types_supported":
    ["code", "code token"],
  "service_documentation":
    "http://server.example.com/service_documentation.html",
  "ui_locales_supported":
    ["en-US", "en-GB", "en-CA", "fr-FR", "fr-CA"]
 }
```

---
# Authorization Server Metadata Discovery

4. The client sends a request to the authorization server's metadata endpoint to retrieve its metadata
5. The client uses the metadata to initiate the PKCE flow with the authorization server