{{- define "prom-test-app.name" -}}
prom-test-app
{{- end }}

{{- define "prom-test-app.fullname" -}}
{{ include "prom-test-app.name" . }}
{{- end }}
