package dsquare;

import dsquare.geom.Vertex;
import dsquare.geom.Square;

class DiamondSquare {

	public var vertices:Array<Vertex> = new Array<Vertex>();
	private var deviation:Float;

	public function new(square:Square, deviation:Float = 1.0) {
		this.vertices = square.toArray();
		this.deviation = deviation;
	}

	/**
	 * Generates N iterations of the algorithm, modifies this.vertices
	 *
	 * @param: nIterations[Int] number of iterations to apply
	 * @param: squares[Array<Square>] starting squares, used internally and defaults to null, will use this.vertices automatically
	**/
	public function gen(nIterations:Int = 1, squares:Array<Square> = null):Void {
		if (squares == null) {
			squares = new Array<Square>();
			squares.push(new Square(this.vertices));
		}
		for(i in 0...nIterations) {
			var mids:Array<Vertex> = new Array<Vertex>();
			for(s in squares) {
				var mid = s.getMidpoint();
				mid.z += (Math.random() - 0.5) * deviation;
				mids.push(mid);
				this.vertices.push(mid);
			}
			var newSquares = squareStep(squares);
			nIterations--;
			if (nIterations == 0) return;
			gen(nIterations, newSquares);
		}
	}

	private function squareStep(squares:Array<Square>):Array<Square> {
		var result = new Array<Square>();
		for(s in squares) {
			var mid = s.getMidpoint();
			var edgeMids = s.getEdgeMidpoints();
			for(p in edgeMids) {
				this.vertices.push(p);
			}
			var sq1 = new Square([s.v0, edgeMids[0], mid, edgeMids[3]]);
			var sq2 = new Square([edgeMids[0], s.v1, edgeMids[1], mid]);
			var sq3 = new Square([mid, edgeMids[1], s.v2, edgeMids[2]]);
			var sq4 = new Square([edgeMids[3], mid, edgeMids[2], s.v3]);
			result = result.concat([sq1, sq2, sq3, sq4]);
		}
		return result;
	}
}
