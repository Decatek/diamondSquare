import massive.munit.TestSuite;

import dsquare.geom.VertexTest;
import dsquare.geom.SquareTest;

/**
 * Auto generated Test Suite for MassiveUnit.
 * Refer to munit command line tool for more information (haxelib run munit)
 */

class TestSuite extends massive.munit.TestSuite
{		

	public function new()
	{
		super();

		add(dsquare.geom.VertexTest);
		add(dsquare.geom.SquareTest);
	}
}
