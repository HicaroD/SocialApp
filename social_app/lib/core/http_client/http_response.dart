class HttpResponse {
  final Map<String, dynamic> body;
  final int statusCode;

  HttpResponse({
    required this.body,
    required this.statusCode,
  });
}
