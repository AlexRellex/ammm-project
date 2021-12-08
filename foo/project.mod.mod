// PLEASE ONLY CHANGE THIS FILE WHERE INDICATED.

int n = ...;
int m = ...;

range V = 1..n;
range W = 1..m;

float G[V][V] = ...; // The matrix is symmetric as the graph is undirected.
float H[W][W] = ...; // The matrix is symmetric as the graph is undirected.

// Define here your decision variables and any other auxiliary data.
// You can run an execute block if needed.

minimize // Write here the objective function.

subject to {

    // Write here the constraints.

}

execute {
    
    for (var x in W) {
	var fx = 0;
  	for (var u in V) {
  	    if (a[x][u] == 1) fx = u;
    	}
	writeln("f(" + x + ") = " + fx);
    }
}
