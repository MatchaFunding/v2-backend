#ifndef POSTULACION_H
#define POSTULACION_H

#include "utils.h"

char* VerTodasLasPostulaciones(const char *url);
enum MHD_Result URLPostulacion
(const char *url, const char *method, struct MHD_Connection *conn);

#endif
