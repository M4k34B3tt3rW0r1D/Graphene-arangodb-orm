query{
  allEmployees(first:1, after:"YXJyYXljb25uZWN0aW9uOjE="){
    pageInfo {
      startCursor,
      hasNextPage,
      hasPreviousPage,
      endCursor
    },
    edges{
      node{
        name,
        role{
          id,
          Key,
          name
        },
        department{
          name,
        }
      }
    }
  }
}

