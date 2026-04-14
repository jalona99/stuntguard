import 'package:flutter_test/flutter_test.dart';

import 'package:stuntguard/main.dart';

void main() {
  testWidgets('App loads successfully', (WidgetTester tester) async {
    // Build our app and trigger a frame.
    await tester.pumpWidget(const StuntGuardApp());

    // Verify that the app title is displayed
    expect(find.text('StuntGuard'), findsOneWidget);

    // Verify welcome text is shown
    expect(find.textContaining('Welcome to StuntGuard'), findsOneWidget);
  });
}