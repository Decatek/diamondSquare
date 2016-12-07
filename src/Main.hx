package;

import kha.System;

class Main {
	public static function main() {
		System.init({title: "DiamondSquare", width: 1024, height: 1024}, function () {
			new Example();
		});
	}
}
