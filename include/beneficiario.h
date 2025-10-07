#ifndef BENEFICIARIO_H
#define BENEFICIARIO_H

#include "utils.h"

HTTP_response VerTodosLosBeneficiarios(const char *url);
HTTP_response VerSoloUnBeneficiario(const char *id);
HTTP_response URLBeneficiario(const char *url, const char *method, const char *body);

#endif
