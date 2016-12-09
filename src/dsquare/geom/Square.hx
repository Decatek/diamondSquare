package dsquare.geom;

class Square {

	public function new(verts:Array<Vertex>) {
		v0 = verts[0];
		v1 = verts[1];
		v2 = verts[2];
		v3 = verts[3];
	}

	public var v0:Vertex;
	public var v1:Vertex;
	public var v2:Vertex;
	public var v3:Vertex;

	/**
	 * Get the midpoint of the square
	 *
	 * @returns: Vertex
	**/
	public function getMidpoint():Vertex {
		var x:Float = (v0.x + v1.x) / 2;
		var y:Float = (v0.y + v2.y) / 2;
		var z:Float = (v0.z + v1.z + v2.z + v3.z) / 4;
		return new Vertex(x, y, z);
	}

	/**
	 * Gets all the midpoints of the edges of the square
	 *
	 * @returns: Array<Vertex> all the midpoints, ordered from top-left clockwise
	**/
	public function getEdgeMidpoints():Array<Vertex> {
		var mids = new Array<Vertex>();
		for(i in 0...4) {
			var arr = this.toArray();
			mids[i] = Vertex.getMid(arr[i], arr[(i+1) % 4]);
		}
		return mids;
	}

	/**
	 * Converts the square to an array containing all vertices
	 *
	 * @returns: Array<Vertex> all the vertices orderer clockwise starting from top-left
	**/
	public function toArray():Array<Vertex> {
		var arr:Array<Vertex> = new Array<Vertex>();
		arr[0] = v0;
		arr[1] = v1;
		arr[2] = v2;
		arr[3] = v3;
		return arr;
	}
}
