import 'package:flutter_modular/flutter_modular.dart';

import 'app/presenter/pages/login/login_page.dart';
import 'app/presenter/pages/register/register_page.dart';
import 'core/http_client/http_client.dart';
import 'utils/api_endpoints.dart';

class AppModule extends Module {
  final client = HttpClient(baseUrl: BASE_URL);

  @override
  List<Bind> get binds => [Bind.singleton((_) => client)];

  @override
  final List<ModularRoute> routes = [
    ChildRoute("/", child: (_, __) => LoginPage()),
    ChildRoute("/sign-up", child: (_, __) => RegisterPage()),
  ];
}
