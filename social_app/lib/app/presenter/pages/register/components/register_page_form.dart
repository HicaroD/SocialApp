import 'package:flutter/material.dart';
import 'package:flutter_modular/flutter_modular.dart';

import '../../../widgets/form_field.dart';

class RegisterPageForm extends StatefulWidget {
  final Size screenSize;

  const RegisterPageForm({
    Key? key,
    required this.screenSize,
  }) : super(key: key);

  @override
  State<RegisterPageForm> createState() => _RegisterPageFormState();
}

class _RegisterPageFormState extends State<RegisterPageForm> {
  Size get screenSize => widget.screenSize;

  final registerFormKey = GlobalKey<FormState>();
  final usernameController = TextEditingController();
  final ageController = TextEditingController();
  final descriptionController = TextEditingController();

  @override
  Widget build(BuildContext context) {
    return Column(
      children: <Widget>[
        Center(
          child: Form(
            key: registerFormKey,
            child: SizedBox(
              width: screenSize.width * 0.8,
              child: Column(
                children: [
                  CustomFormField(
                    labelText: "Username",
                    controller: usernameController,
                  ),
                  CustomFormField(
                    labelText: "Age",
                    controller: ageController,
                    keyboardType: TextInputType.number,
                  ),
                  CustomFormField(
                    labelText: "Description",
                    controller: descriptionController,
                  ),
                  ElevatedButton(
                    // TODO: interact with API to create a user
                    onPressed: () {
                      print(usernameController.text);
                      print(ageController.text);
                      print(descriptionController.text);
                    },
                    child: const Text("Sign up"),
                  ),
                ],
              ),
            ),
          ),
        ),
        TextButton(
          onPressed: () => Modular.to.navigate("/"),
          child: const Text("Already have an account? Sign in"),
        ),
      ],
    );
  }
}
