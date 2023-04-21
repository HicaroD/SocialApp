import 'package:flutter/material.dart';
import 'package:flutter_modular/flutter_modular.dart';
import '../../widgets/form_field.dart';

class LoginPage extends StatelessWidget {
  LoginPage({Key? key}) : super(key: key);

  final loginFormKey = GlobalKey<FormState>();
  final usernameController = TextEditingController();

  @override
  Widget build(BuildContext context) {
    Size screenSize = MediaQuery.of(context).size;

    return Scaffold(
      backgroundColor: Colors.white,
      appBar: AppBar(
        backgroundColor: Colors.blue,
        title: const Text("SocialApp"),
      ),
      body: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: <Widget>[
          Center(
            child: Form(
              key: loginFormKey,
              child: SizedBox(
                width: screenSize.width * 0.8,
                child: Column(
                  children: [
                    CustomFormField(
                      labelText: "Username",
                      controller: usernameController,
                    ),
                    ElevatedButton(
                      // TODO: interact with API to login a user
                      onPressed: () {
                        print(usernameController.text);
                      },
                      child: const Text("Sign in"),
                    ),
                  ],
                ),
              ),
            ),
          ),
          TextButton(
            onPressed: () => Modular.to.navigate("/sign-up"),
            child: const Text("Create an account"),
          ),
        ],
      ),
    );
  }
}
