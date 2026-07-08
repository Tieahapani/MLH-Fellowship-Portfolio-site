#!/bin/bash

echo "Testing POST /api/timeline_post..."
RESPONSE=$(curl -s -X POST http://localhost:5000/api/timeline_post \
  -d "name=Test User" \
  -d "email=test@example.com" \
  -d "content=This is a random test post $(date)")

echo "POST Response: $RESPONSE"

ID=$(echo $RESPONSE | python3 -c "import sys, json; print(json.load(sys.stdin)['id'])")
echo "Created post with ID: $ID"

echo ""
echo "Testing GET /api/timeline_post..."
GET_RESPONSE=$(curl -s http://localhost:5000/api/timeline_post)
echo "GET Response: $GET_RESPONSE"

if echo $GET_RESPONSE | grep -q "Test User"; then
    echo ""
    echo "✅ POST and GET verified successfully!"
else
    echo ""
    echo "❌ Test failed — post not found in GET response"
    exit 1
fi

echo ""
echo "Cleaning up — deleting post ID $ID..."
DELETE_RESPONSE=$(curl -s -X DELETE http://localhost:5000/api/timeline_post/$ID)
echo "DELETE Response: $DELETE_RESPONSE"
echo "✅ Cleanup done!"
