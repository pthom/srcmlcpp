#include "mylib/api_marker.h"

namespace SomeNamespace                                        // MY_API
{
    struct ParentStruct                                        // MY_API
    {
        struct InnerStruct                                     // MY_API
        {
            int value;

            InnerStruct(int value = 0) : value(value) {}
            MY_API int add(int a, int b) { return a + b; }
        };

//        enum class InnerEnum                                   // MY_API
//        {
//            Zero = 0,
//            One,
//            Two
//        };

        int a = 1;
        InnerStruct inner_struct;
//        InnerEnum inner_enum;
    };
} // namespace SomeNamespace
