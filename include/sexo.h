#ifndef SEXO_H
#define SEXO_H

#include "utils.h"

HTTP_response VerSexos(const char *url);
HTTP_response URLSexo(const char *url, const char *method, const char *body);

#endif
