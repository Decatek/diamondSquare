package dsquare.geom;

import massive.munit.util.Timer;
import massive.munit.Assert;
import massive.munit.async.AsyncFactory;


class SquareTest 
{
	var v0:Vertex;
	var v1:Vertex;
	var v2:Vertex;
	var v3:Vertex;
	var verts:Array<Vertex>;

	public function new() 
	{
		
	}
	
	@BeforeClass
	public function beforeClass():Void
	{
	}
	
	@AfterClass
	public function afterClass():Void
	{
	}
	
	@Before
	public function setup():Void
	{
		v0 = new Vertex(0, 0);
		v1 = new Vertex(1, 0);
		v2 = new Vertex(1, 1);
		v3 = new Vertex(0, 1);
		verts = [v0, v1, v2, v3];
	}
	
	@After
	public function tearDown():Void
	{
	}
	
	@Test
	public function shouldCreateSquare():Void
	{
		var square = new Square(verts);
		Assert.areEqual(square.v0.x, 0);
		Assert.areEqual(square.v0.y, 0);
		Assert.areEqual(square.v1.x, 1);
		Assert.areEqual(square.v1.y, 0);
		Assert.areEqual(square.v2.x, 1);
		Assert.areEqual(square.v2.y, 1);
		Assert.areEqual(square.v3.x, 0);
		Assert.areEqual(square.v3.y, 1);
	}

	@Test
	public function shouldGetMidpoint():Void
	{
		var square = new Square(verts);
		var mid = square.getMidpoint();
		Assert.areEqual(mid.x, 0.5);
		Assert.areEqual(mid.y, 0.5);
	}

	@Test
	public function shouldGetEdgeMidpoints():Void
	{
		var s = new Square(verts);
		var mids = s.getEdgeMidpoints();
		Assert.areEqual(mids[0].x, 0.5);
		Assert.areEqual(mids[0].y, 0);
		Assert.areEqual(mids[1].x, 1);
		Assert.areEqual(mids[1].y, 0.5);
		Assert.areEqual(mids[2].x, 0.5);
		Assert.areEqual(mids[2].y, 1);
		Assert.areEqual(mids[3].x, 0);
		Assert.areEqual(mids[3].y, 0.5);
	}
}
