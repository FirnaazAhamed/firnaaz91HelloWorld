/*
A KBase module: firnaaz91HelloWorld
*/

module firnaaz91HelloWorld {
    typedef structure {
        string report_name;
        string report_ref;
    } ReportResults;

    /*
        This example function accepts any number of parameters and returns results in a KBaseReport
    */
    funcdef run_firnaaz91HelloWorld(mapping<string,UnspecifiedObject> params) returns (ReportResults output) authentication required;
    
    /*
        This is the new function which I'm creating for example. 
    */
    funcdef run_firnaaz91HelloWorld_new(mapping<string,UnspecifiedObject> params) returns (ReportResults output) authentication required;

};
