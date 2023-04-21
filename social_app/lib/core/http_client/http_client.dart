import 'dart:convert';
import 'package:http/http.dart' as http;

import '../../utils/api_endpoints.dart';
import 'http_client.interface.dart';
import 'http_response.dart';

class HttpClient implements IHttpClient {
  final _httpClient = http.Client();
  final String baseUrl;

  HttpClient({required this.baseUrl});

  Uri getUri(String url, {Map<String, dynamic>? queryParameters}) {
    return Uri(
      scheme: "https",
      host: BASE_URL,
      path: url,
      queryParameters: {}, // TODO: implement queryParameters (when I need it)
    );
  }

  @override
  Future<HttpResponse> get(
    String url, {
    Map<String, String>? headers,
  }) async {
    Uri uri = getUri(url);

    final http.Response response = await _httpClient.get(
      uri,
      headers: headers ?? {},
    );

    return HttpResponse(
      body: json.decode(response.body),
      statusCode: response.statusCode,
    );
  }

  @override
  Future<HttpResponse> post(
    String url, {
    Map<String, String>? headers,
    Map<String, String>? body,
  }) async {
    Uri uri = getUri(url);

    final http.Response response = await _httpClient.post(
      uri,
      headers: headers,
      body: jsonEncode(body),
    );

    return HttpResponse(
      body: json.decode(response.body),
      statusCode: response.statusCode,
    );
  }

  @override
  Future<HttpResponse> put(
    String url, {
    Map<String, String>? headers,
    Map<String, String>? body,
  }) async {
    Uri uri = getUri(url);

    final http.Response response = await _httpClient.put(
      uri,
      headers: headers,
      body: jsonEncode(body),
    );

    return HttpResponse(
      body: json.decode(response.body),
      statusCode: response.statusCode,
    );
  }

  @override
  Future<HttpResponse> delete(
    String url, {
    Map<String, String>? headers,
  }) async {
    Uri uri = getUri(url);

    final http.Response response = await _httpClient.delete(
      uri,
      headers: headers,
    );

    return HttpResponse(
      body: json.decode(response.body),
      statusCode: response.statusCode,
    );
  }

  @override
  Future<HttpResponse> patch(
    String url, {
    Map<String, String>? headers,
    Map<String, String>? body,
  }) async {
    Uri uri = getUri(url);

    final http.Response response = await _httpClient.delete(
      uri,
      headers: headers,
      body: jsonEncode(body),
    );

    return HttpResponse(
      body: json.decode(response.body),
      statusCode: response.statusCode,
    );
  }
}
