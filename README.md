
# WeasyPrint HTML to Fillable-PDF/PNG Microservice

The [docker-weasyprint](https://github.com/hassananv/docker-weasyprint) project bundles [Weasyprint](http://weasyprint.org/) and [BCDevOps/docker-weasyprint](https://github.com/BCDevOps/docker-weasyprint) into an easy to use, OpenShift compatible, HTML to Fillable-PDF/PNG microservice with a simple REST interface.

# Images

Pre-built images can be found here; [hassananv/weasyprint](https://hub.docker.com/r/hassananv/weasyprint)

`docker pull hassananv/weasyprint`

# Usage - Docker Example

Run the docker image, exposing port 5001

```
docker run -p 5001:5001 hassananv/weasyprint
```

A `POST` to `/pdf` on port 5001 with an html body will result in a response containing a Fillable-PDF. The filename may be set using a query parameter, e.g.:

```
curl -v -X POST -d @test.html -JLO http://127.0.0.1:5001/pdf?filename=result.pdf
```

This example will use the file `test.html` and return a response with `Content-Type: application/pdf` and `Content-Disposition: inline; filename=result.pdf` headers.  The body of the response will be the PDF rendering of the html document. To generate a png, make a call to `/png` instead

In addition `/health` is a health check endpoint and a `GET` returns 'ok'.

# Usage - Sample Html Fillable Element

The following is an example of an input field. 

```
<input id="interactive-text-1" style="width:6rem; height:1.5rem; " alt="Test Text" />
```
The `id` of the element should start with `interactive-text-` and must be unique.
The element's `height` and `width` should be defined.
The `alt` attribute is optional. 