// PLEASE ONLY CHANGE THIS FILE WHERE INDICATED.

int n = ...;
int m = ...;

range V = 1..n;
range W = 1..m;

float G[V][V] = ...; // The matrix is symmetric as the graph is undirected.
float H[W][W] = ...; // The matrix is symmetric as the graph is undirected.

// Define here your decision variables and any other auxiliary data.
// You can run an execute block if needed.

int GConnection[v1 in V, v2 in V] = (G[v1,v2] == 0) ? 0 : 1; //unweighted edge matrix
int HConnection[w1 in W, w2 in W] = (H[w1,w2] == 0) ? 0 : 1; //unweighted edge matrix

dvar boolean edge[W,W,V,V]; // edge assignment matrix 
dvar boolean a[W,V]; // node assignment matrix
dvar float+ z;

minimize z;

subject to {
	z == sum(w1 in W, w2 in W, v1 in V, v2 in V) edge[w1,w2,v1,v2] * abs(H[w1,w2]-G[v1,v2])/2;  
    //EveryShapeNodeHasToBeAssigned: 
    forall(w in W) sum(v in V) a[w,v] == 1;
    //InjectivityOfNodes: 
    forall(v in V) sum(w in W) a[w,v] <= 1;
    //EdgesExistInShapeAndHaveToBeInserted: 
    forall(w1 in W, w2 in W) sum(v1 in V, v2 in V) edge[w1,w2,v1,v2] == HConnection[w1,w2];
    //EdgesHaveToExistInImage: 
    forall(v1 in V, v2 in V) sum(w1 in W, w2 in W) edge[w1,w2,v1,v2] <= GConnection[v1,v2];
    //TieEdgesToNodes1_1: 
    forall(v1 in V, v2 in V, w1 in W, w2 in W) a[w1,v1] + a[w2,v1] >= edge[w1,w2,v1,v2];
    //TieEdgesToNodes1_2: 
    forall(v1 in V, v2 in V, w1 in W, w2 in W) a[w1,v1] + a[w1,v2] >= edge[w1,w2,v1,v2];
    //TieEdgesToNodes1_3: 
    forall(v1 in V, v2 in V, w1 in W, w2 in W) a[w2,v2] + a[w2,v1] >= edge[w1,w2,v1,v2];
    //TieEdgesToNodes1_4: 
    forall(v1 in V, v2 in V, w1 in W, w2 in W) a[w2,v2] + a[w1,v2] >= edge[w1,w2,v1,v2];
    //ImageNodesCantHaveMoreEdges: 
    forall(v1 in V, v2 in V, w1 in W, w2 in W) 2 + HConnection[w1,w2] >= GConnection[v1,v2] + a[w1,v1]+a[w2,v2];

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
