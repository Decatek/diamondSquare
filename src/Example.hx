package;

import kha.Framebuffer;
import kha.Scheduler;
import kha.System;
import dsquare.DiamondSquare;
import dsquare.geom.Vertex;
import dsquare.geom.Square;

class Example {

	var dsquare:DiamondSquare;
	var squares:Array<Square> = [];

	static var ITERATIONS:Int = 5;

	static var SIZE:Float = 1024;

	public function new() {
		System.notifyOnRender(render);
		Scheduler.addTimeTask(update, 0, 1 / 60);

		var a0:Vertex = new Vertex(0, 0);
		var a1:Vertex = new Vertex(SIZE, 0);
		var a2:Vertex = new Vertex(SIZE, SIZE);
		var a3:Vertex = new Vertex(0, SIZE);
		var sq1 = new Square([a0, a1, a2, a3]);
		squares.push(sq1);

		dsquare = new DiamondSquare(sq1, 10);
		dsquare.gen(ITERATIONS);
	}

	function update(): Void {
	}

	function render(framebuffer: Framebuffer): Void {
		var g = framebuffer.g2;
		g.begin();
		for(v in dsquare.vertices) {
			g.fillRect(v.x, v.y, 10 + v.z, 10 + v.z);
		}
		g.end();
	}
}
