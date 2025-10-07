#ifndef INSTRUMENTO_H
#define INSTRUMENTO_H

#include "utils.h"

HTTP_response VerTodosLosInstrumentos(const char *url);
HTTP_response VerSoloUnInstrumento(const char *id);
HTTP_response URLInstrumento(const char *url, const char *method, const char *body);

#endif
