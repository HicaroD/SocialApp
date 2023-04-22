import 'package:flutter/material.dart';
import 'package:flutter/services.dart';

class CustomFormField extends StatefulWidget {
  TextEditingController controller;
  TextInputType? keyboardType;
  String labelText;

  CustomFormField({
    Key? key,
    required this.controller,
    required this.labelText,
    this.keyboardType,
  }) : super(key: key);

  @override
  State<CustomFormField> createState() => _CustomFormFieldState();
}

class _CustomFormFieldState extends State<CustomFormField> {
  TextEditingController get controller => widget.controller;
  TextInputType? get keyboardType => widget.keyboardType;
  String get labelText => widget.labelText;

  @override
  Widget build(BuildContext context) {
    return TextFormField(
      controller: controller,
      decoration: InputDecoration(
        labelText: labelText,
        labelStyle: TextStyle(
          color: Colors.grey[800],
          fontWeight: FontWeight.bold,
        ),
        focusedBorder: const UnderlineInputBorder(
          borderSide: BorderSide(color: Colors.blue),
        ),
      ),
      style: const TextStyle(
        color: Colors.black,
        fontSize: 16,
      ),
      keyboardType: keyboardType,
    );
  }
}
