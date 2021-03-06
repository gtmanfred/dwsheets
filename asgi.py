import os

import uvicorn


if __name__ == '__main__':
    uvicorn.run(
        'dwsheets.app:create_app',
        host='0.0.0.0', port=int(os.getenv('PORT', 8000)),
        reload=True,
        reload_dirs=['dwsheets'],
        factory=True,
    )
