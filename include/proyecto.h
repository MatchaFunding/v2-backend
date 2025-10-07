#ifndef PROYECTO_H
#define PROYECTO_H

#include "utils.h"

HTTP_response VerTodosLosProyectos(const char *url);
HTTP_response VerSoloUnProyecto(const char *id);
HTTP_response URLProyecto(const char *url, const char *method, const char *body);

#endif
