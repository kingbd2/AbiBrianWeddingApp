import axios from 'axios';

// const protocol_result = location.protocol;
// const slashes = protocol_result.concat('//');
// const host = slashes.concat(window.location.hostname);
// const host_with_port = host.concat(':8000');
const dev_host_with_port = '//localhost:8000';
const prod_host_with_port = '//abiellaandbriangetmarried.ca';
const base_path = prod_host_with_port.concat('/api/v1/');
// const base_path = prod_host_with_port.concat('/api/v1/');

const CSRF_COOKIE_NAME = 'csrftoken';
const CSRF_HEADER_NAME = 'X-CSRFToken';

const session = axios.create({
  withCredentials: true,
  xsrfCookieName: CSRF_COOKIE_NAME,
  xsrfHeaderName: CSRF_HEADER_NAME,
  baseURL: base_path,
});

export default session;
