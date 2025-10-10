#ifndef PERSONA_H
#define PERSONA_H

#include "utils.h"

char* VerTodasLasPersonas(const char *url);
enum MHD_Result URLPersona
(const char *url, const char *method, struct MHD_Connection *conn);

#endif
