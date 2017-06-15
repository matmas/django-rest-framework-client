""""
Django REST Framework client
https://github.com/qvantel/django-rest-framework-client
Copyright (c) 2017, Qvantel
All rights reserved.
Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:
    * Redistributions of source code must retain the above copyright
      notice, this list of conditions and the following disclaimer.
    * Redistributions in binary form must reproduce the above copyright
      notice, this list of conditions and the following disclaimer in the
      documentation and/or other materials provided with the distribution.
    * Neither the name of the Qvantel nor the
      names of its contributors may be used to endorse or promote products
      derived from this software without specific prior written permission.
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL QVANTEL BE LIABLE FOR ANY
DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""


class ServerResponseException(Exception):
    """
    Indicates the HTTP status code other than the ones implemented by separate exception class
    such as BadRequestResponse, BadGatewayResponse or ConflictRespose.
    """
    pass


class BadRequestResponse(ServerResponseException):
    """
    Indicates the HTTP status code 400.
    """
    pass


class BadGatewayResponse(ServerResponseException):
    """
    Indicates the HTTP status code 502.
    """
    pass


class ConflictRespose(ServerResponseException):
    """
    Indicates the HTTP status code 409.
    """
    pass


class NotPersistedError(Exception):
    """
    Occurs when deleting or refreshing instances unknown by the server.
    """
    pass


class FieldTypeMismatch(Exception):
    """
    Occurs when a server-side serializer field differs semantically from the client side field.
    """
    pass


class NoneValueInParams(Exception):
    """
    Occurs when passing None to a filter argument instead of using something__isnull=True.
    """
    pass